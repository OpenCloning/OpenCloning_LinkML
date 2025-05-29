from typing import Dict, Callable, Tuple, Any, Optional
from packaging import version
import copy

from ..datamodel import CloningStrategy
from .._version import __version__

# Migration registry - maps version ranges to migration functions
# Format: (start_version, end_version) -> migration_function

MigrationDict = dict[tuple[str, str], Callable]


# Import migration modules to register migrations
def load_migrations() -> MigrationDict:
    """Load all migration modules to register migrations."""

    # Import migration modules
    from .transformations.v0_2_6_1_to_v_0_2_8 import migrate_0_2_6_1_to_0_2_8  # noqa: F401
    from .transformations.v0_2_8_to_v0_2_9 import migrate_0_2_8_to_0_2_9  # noqa: F401

    return {
        ("0.2.6.1", "0.2.8"): migrate_0_2_6_1_to_0_2_8,
        ("0.2.8", "0.2.9"): migrate_0_2_8_to_0_2_9,
    }


def migrate(data: Dict[str, Any], target_version: Optional[str] = None) -> Dict[str, Any] | None:
    """
    Migrate data from its current version to the target version.

    Args:
        data: Data to migrate (must contain "schema_version" field)
        target_version: Target version (defaults to latest available)

    Returns:
        Migrated data dictionary
    """
    use_latest = False
    if target_version is None:
        target_version = __version__
        use_latest = True

    migration_dict = load_migrations()
    current_version = data.get("schema_version")
    if not current_version:
        current_version = "0.2.6.1"

    # No migration needed if already at target version
    if current_version == target_version:
        return None

    # Make a copy to avoid modifying the original
    result = copy.deepcopy(data)

    # Continue migrating until we reach the target version
    if "schema_version" not in result:
        current_version = "0.2.6.1"
    else:
        current_version = result["schema_version"]

    while version.parse(current_version) < version.parse(target_version):
        next_migration = _find_next_migration(current_version, target_version, migration_dict)
        if not next_migration:
            break  # No more applicable migrations

        start_ver, current_version = next_migration
        migration_func = migration_dict[(start_ver, current_version)]

        # Apply the migration
        result = migration_func(result)
        result["schema_version"] = current_version  # Update the version

    if use_latest:
        result = CloningStrategy.model_validate(result).model_dump()
        result["schema_version"] = __version__

    return result


def _find_next_migration(
    current_version: str, target_version: str, migration_dict: MigrationDict
) -> Optional[Tuple[str, str]]:
    """Find the next applicable migration step."""
    applicable_migrations = []

    for (start_ver, end_ver), _ in migration_dict.items():
        # Migration is applicable if:
        # 1. Current version is in the range [start_ver, end_ver)
        # 2. End version is closer to or equal to the target version
        if version.parse(start_ver) <= version.parse(current_version) < version.parse(end_ver) and version.parse(
            end_ver
        ) <= version.parse(target_version):
            applicable_migrations.append((start_ver, end_ver))

    if not applicable_migrations:
        return None

    # Choose the migration that gets us closest to the target version
    return max(applicable_migrations, key=lambda x: version.parse(x[1]))

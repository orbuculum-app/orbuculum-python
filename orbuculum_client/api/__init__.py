# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from orbuculum_client.api.account_api import AccountApi
    from orbuculum_client.api.account_permissions_api import AccountPermissionsApi
    from orbuculum_client.api.activity_journal_api import ActivityJournalApi
    from orbuculum_client.api.app_context_api import AppContextApi
    from orbuculum_client.api.authentication_api import AuthenticationApi
    from orbuculum_client.api.bulk_permissions_api import BulkPermissionsApi
    from orbuculum_client.api.connection_api import ConnectionApi
    from orbuculum_client.api.currency_api import CurrencyApi
    from orbuculum_client.api.custom_api import CustomApi
    from orbuculum_client.api.entity_api import EntityApi
    from orbuculum_client.api.entity_permissions_api import EntityPermissionsApi
    from orbuculum_client.api.general_permissions_api import GeneralPermissionsApi
    from orbuculum_client.api.import_api import ImportApi
    from orbuculum_client.api.label_api import LabelApi
    from orbuculum_client.api.label_permissions_api import LabelPermissionsApi
    from orbuculum_client.api.limitation_api import LimitationApi
    from orbuculum_client.api.matching_api import MatchingApi
    from orbuculum_client.api.membership_api import MembershipApi
    from orbuculum_client.api.permission_api import PermissionApi
    from orbuculum_client.api.rate_api import RateApi
    from orbuculum_client.api.reports_api import ReportsApi
    from orbuculum_client.api.role_api import RoleApi
    from orbuculum_client.api.scheduled_transaction_api import ScheduledTransactionApi
    from orbuculum_client.api.selection_api import SelectionApi
    from orbuculum_client.api.system_api import SystemApi
    from orbuculum_client.api.tag_api import TagApi
    from orbuculum_client.api.transaction_api import TransactionApi
    from orbuculum_client.api.user_api import UserApi
    from orbuculum_client.api.user_admin_api import UserAdminApi
    from orbuculum_client.api.workspace_api import WorkspaceApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from orbuculum_client.api.account_api import AccountApi
from orbuculum_client.api.account_permissions_api import AccountPermissionsApi
from orbuculum_client.api.activity_journal_api import ActivityJournalApi
from orbuculum_client.api.app_context_api import AppContextApi
from orbuculum_client.api.authentication_api import AuthenticationApi
from orbuculum_client.api.bulk_permissions_api import BulkPermissionsApi
from orbuculum_client.api.connection_api import ConnectionApi
from orbuculum_client.api.currency_api import CurrencyApi
from orbuculum_client.api.custom_api import CustomApi
from orbuculum_client.api.entity_api import EntityApi
from orbuculum_client.api.entity_permissions_api import EntityPermissionsApi
from orbuculum_client.api.general_permissions_api import GeneralPermissionsApi
from orbuculum_client.api.import_api import ImportApi
from orbuculum_client.api.label_api import LabelApi
from orbuculum_client.api.label_permissions_api import LabelPermissionsApi
from orbuculum_client.api.limitation_api import LimitationApi
from orbuculum_client.api.matching_api import MatchingApi
from orbuculum_client.api.membership_api import MembershipApi
from orbuculum_client.api.permission_api import PermissionApi
from orbuculum_client.api.rate_api import RateApi
from orbuculum_client.api.reports_api import ReportsApi
from orbuculum_client.api.role_api import RoleApi
from orbuculum_client.api.scheduled_transaction_api import ScheduledTransactionApi
from orbuculum_client.api.selection_api import SelectionApi
from orbuculum_client.api.system_api import SystemApi
from orbuculum_client.api.tag_api import TagApi
from orbuculum_client.api.transaction_api import TransactionApi
from orbuculum_client.api.user_api import UserApi
from orbuculum_client.api.user_admin_api import UserAdminApi
from orbuculum_client.api.workspace_api import WorkspaceApi

""",
            name=__name__,
            doc=__doc__,
        )
    )

from .display import green

__all__ = (
    'Projects',
    'Environments',
    'URLTypes',
    'url_patterns',
    'shortcuts',
)


class Projects:
    BANK = 'BANK'
    MRPL = 'MRPL'
    RND = 'RND'


class Environments:
    STAND = 'STAND'
    RC = 'RC'
    PRODUCTION = 'PRODUCTION'


class URLTypes:
    JIRA = 'JIRA'
    K8S = 'K8S'
    LOGHOUSE = 'LOGHOUSE'
    ADMIN = 'ADMIN'
    FRONT = 'FRONT'
    API = 'API'
    GITLAB = 'GITLAB'


shortcuts = {
    URLTypes.JIRA: ('j', 'J' * green + 'IRA'),
    URLTypes.K8S: ('k', 'K' * green + '8S'),
    URLTypes.LOGHOUSE: ('l', 'L' * green + 'OGHOUSE'),
    URLTypes.ADMIN: ('a', 'A' * green + 'DMIN'),
    URLTypes.FRONT: ('f', 'F' * green + 'RONT'),
    URLTypes.API: ('i', 'AP' + 'I' * green),
    URLTypes.GITLAB: ('g', 'G' * green + 'ITLAB'),
}


url_patterns = {
    URLTypes.JIRA: 'https://jira.homecred.it/browse/{issue}',
    URLTypes.K8S: (
        'https://k8s.homecred.it/#!/overview?namespace={issue_lower}'
    ),
    URLTypes.LOGHOUSE: (
        'https://loghouse.homecred.it/query'
        '?query=~app="api"&namespaces[]={issue_lower}&shown_keys[]=log'
    ),
    URLTypes.GITLAB: (
        'https://gitlab.homecred.it/hc-backend/hc_market/tree/{full_issue}'
    ),
    URLTypes.ADMIN: {
        Environments.STAND: {
            Projects.BANK: 'https://admin-hcb-bank-{task}.homecred.it',
            Projects.MRPL: 'https://admin-mrpl-{task}.homecred.it',
        },
        Environments.RC: {
            Projects.BANK: 'https://rc.admin.bank.homecredit.ru',
            Projects.MRPL: 'http://rc.admin.market.homecredit.ru',
        },
        Environments.PRODUCTION: {
            Projects.BANK: 'https://admin.bank.homecredit.ru',
            Projects.MRPL: 'http://admin.market.homecredit.ru',
        },
    },
    URLTypes.FRONT: {
        Environments.STAND: {
            Projects.BANK: 'https://hcb-bank-{task}.homecred.it/',
            Projects.MRPL: 'https://market-mrpl-{task}.homecred.it',
        },
        Environments.RC: {
            Projects.BANK: 'https://rc.homecredit.ru/',
            Projects.MRPL: 'https://spb-market.rc.homecredit.ru/',
        },
        Environments.PRODUCTION: {
            Projects.BANK: 'https://www.homecredit.ru',
            Projects.MRPL: 'http://market.homecredit.ru',
        },
    },
    URLTypes.API: {
        Environments.STAND: {
            Projects.BANK: 'https://api-hcb-bank-{task}.homecred.it',
            Projects.MRPL: 'https://api-mrpl-{task}.homecred.it',
        },
        Environments.RC: {
            Projects.BANK: 'https://rc.api.bank.homecredit.ru',
            Projects.MRPL: 'http://rc.api.market.homecredit.ru',
        },
        Environments.PRODUCTION: {
            Projects.BANK: 'https://api.bank.homecredit.ru',
            Projects.MRPL: 'http://api.market.homecredit.ru',
        },
    },
}

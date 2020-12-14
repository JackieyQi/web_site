# coding:utf8

from appconf import AppConf


# basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(
#                            os.path.dirname(__file__)))))

class PostAppConf(AppConf):
    # PAGINATE_BY = ALL_CONFIG.get("POSTAPPCONF", "paginate")

    class Meta:
        prefix = "post"

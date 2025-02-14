import llm
from llm.default_plugins.openai_models import Chat

# Try to import AsyncChat, but don't fail if it's not available
try:
    from llm.default_plugins.openai_models import AsyncChat

    HAS_ASYNC = True
except ImportError:
    HAS_ASYNC = False

MODELS = (
    "anthropic/claude-3.5-sonnet",
    "deepseek-ai/deepseek-r1",
)


class ReplicateChat(Chat):
    needs_key = "replicate"
    key_env_var = "LLM_REPLICATE_KEY"

    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=f"replicate/{model_name}",
            api_base="https://openai-proxy.replicate.com/v1",
        )

    def __str__(self):
        return "Replicate: {}".format(self.model_id)


# Only define AsyncChat class if async support is available
if HAS_ASYNC:

    class ReplicateAsyncChat(AsyncChat):
        needs_key = "replicate"
        key_env_var = "LLM_REPLICATE_KEY"

        def __init__(self, model_name):
            super().__init__(
                model_name=model_name,
                model_id=f"replicate/{model_name}",
                api_base="https://openai-proxy.replicate.com/v1",
            )

        def __str__(self):
            return "Replicate: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    # Only do this if the key is set
    key = llm.get_key("", "replicate", ReplicateChat.key_env_var)
    if not key:
        return
    for model_id in MODELS:
        if HAS_ASYNC:
            register(
                ReplicateChat(model_id),
                ReplicateAsyncChat(model_id),
            )
        else:
            register(ReplicateChat(model_id))

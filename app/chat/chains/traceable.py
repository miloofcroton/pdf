from uuid import UUID

from langfuse.langchain import CallbackHandler


class TraceableChain:
  def __call__(self, *args, **kwargs):
    # Convert UUID to 32-char hex for OTel trace ID.
    # Recover with: str(uuid.UUID(trace_id))
    trace_id = UUID(self.metadata["conversation_id"]).hex
    handler = CallbackHandler(
      trace_context={"trace_id": trace_id},
      update_trace=True,
    )
    callbacks = kwargs.get("callbacks", [])
    callbacks.append(handler)
    kwargs["callbacks"] = callbacks

    return super().__call__(*args, **kwargs)

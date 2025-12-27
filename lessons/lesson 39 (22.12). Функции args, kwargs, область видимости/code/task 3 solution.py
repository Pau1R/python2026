def make_dispatcher():
    storage = []
    meta = {}

    def dispatch(action, *args, **kwargs):
        nonlocal storage, meta

        if action == "add":
            if not args:
                raise ValueError("add requires at least one positional argument")
            items = [str(x) for x in args]
            storage.extend(items)
            if "source" in kwargs:
                meta["last_source"] = kwargs["source"]
            return

        elif action == "remove":
            item = kwargs.get("item")
            if item is None:
                raise ValueError("remove requires named argument 'item'")
            if item in storage:
                storage.remove(item)
            else:
                print(f"Warning: item not found: {item}")
            return

        elif action == "stats":
            result = {
                "count": len(storage),
                "items": list(storage),
            }
            if kwargs.get("detailed"):
                result["preview"] = storage[:3]
                result["meta"] = dict(meta)
            return result

        else:
            raise ValueError(f"Unknown action: {action}")

    return dispatch


# usage example
dispatcher = make_dispatcher()
dispatcher("add", *["alpha", "beta"], source="cli")
dispatcher("remove", item="beta")
print(dispatcher("stats", detailed=True))
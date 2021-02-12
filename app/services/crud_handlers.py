def update(request_json, model, model_id):
    try:
        found_entity = model.query.get(model_id)

        for key, value in request_json.items():
            setattr(found_entity, key, value)

        found_entity.save(True)
        return found_entity

    except Exception as error:
        print(error)
        return {'msg': str(error)}

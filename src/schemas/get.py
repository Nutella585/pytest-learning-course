GET_SCHEMA = {
    "type"      : "object",
    "properties": {
        "id"        : { "type" : "number", },
        "name"      : { "type" : "string", },
        "username"  : { "type" : "string", },
        "email"     : { "type" : "string", },
        "address"   : { "type" : "object", },
        "phone"     : { "type" : "string", },
        "website"   : { "type" : "string", },
        "company"   : { "type" : "object", },
    },
    "required"  : ["id", "name", "username", "email"]
}

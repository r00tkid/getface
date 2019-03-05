function Collections() {
}

Collections.prototype.collectObject = function (object, ...keys) {
    if (!keys || !keys[0]) return {};

    let new_object = {};

    for (let i = 0; i < keys.length; i++) {
        if (object.hasOwnProperty(keys[i])) {
            new_object[keys[i]] = object[keys[i]];
        }
    }

    return new_object;
};

export default new Collections();
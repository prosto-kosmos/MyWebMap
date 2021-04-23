class Entity{
    constructor(entity_id) {
        this._entity_id = entity_id;
        this._enabled = 'false';
        this._number = 'xx000x00';
        this._model = 'Brand not defined';
        this._params = new Map();
        this._streamlinks = new Map();
        this._position_n = 0.0;
        this._position_e = 0.0;
        this._iconFeature = new ol.Feature();
        this._popup = new ol.Overlay({});
    }

    get getID() {
        return this._entity_id;
    }
    set setID(value) {
        this._entity_id = value;
    }

    get getEnabled() {
        return this._enabled;
    }
    set setEnabled(value) {
        this._enabled = value;
    }

    get getNumber() {
        return this._number;
    }
    set setNumber(value) {
        this._number = value;
    }

    get getModel() {
        return this._model;
    }
    set setModel(value) {
        this._model = value;
    }

    get getParams() {
        return this._params;
    }
    set setParams(value) {
        this._params = value;
    }

    get getStreamLinks() {
        return this._streamlinks;
    }
    set setStreamLinks(value) {
        this._streamlinks = value;
    }

    get getPositionN() {
        return this._position_n;
    }
    set setPositionN(value) {
        this._position_n = value;
    }

    get getPositionE() {
        return this._position_e;
    }
    set setPositionE(value) {
        this._position_e = value;
    }

    get getIconFeature() {
        return this._iconFeature;
    }
    set setIconFeature(value) {
        this._iconFeature = value;
    }

    get getPopup() {
        return this._popup;
    }
    set setPopup(value) {
        this._popup = value;
    }

}
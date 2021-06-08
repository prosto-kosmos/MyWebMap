class EntityMap extends Map{

    get getIconFeatureList(){
        var iconFeatureList = [];
        for(var [auto_id, value] of this.entries()) {
            iconFeatureList.push(value.getIconFeature);
        }
        return iconFeatureList;
    }

    get getCountEntity(){
        var count = 0;
        for(var [auto_id, value] of this.entries()) {
            count+=1;
        }
        return count;
    }

    get getIdList(){
        var ids = new Array();
        for(var [auto_id, value] of this.entries()) {
            ids.push(auto_id);
        }
        return ids;
    }

    getNumberById(value){
        return this.get(value).getNumber;
    }

    getModelById(value){
        return this.get(value).getModel;
    }

    getIconFeatureById(value){
        return this.get(value).getIconFeature;
    }

    getPopupById(value){
        return this.get(value).getPopup;
    }
}
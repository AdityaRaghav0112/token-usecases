async function fetchAndProcessExternalApplicationData(externalApiEndpointUrl) {
    try {
        const networkResponseObject = await fetch(externalApiEndpointUrl);
        if (!networkResponseObject.ok) {
            throw new Error(`Network request failed with status code: ${networkResponseObject.status}`);
        }
        const parsedJsonDataPayload = await networkResponseObject.json();
        
        const filteredActiveItemsArray = parsedJsonDataPayload.filter(function(individualDataItemObject) {
            return individualDataItemObject.isActiveStatus === true;
        });
        
        return filteredActiveItemsArray;
    } catch (networkRequestErrorHandler) {
        console.error("An error occurred during the network request:", networkRequestErrorHandler);
        return [];
    }
}

# michelin-map
Retrieve details of restaurants in the Michelin Guide and coerce into an import for a Google Maps layer


## Idea
- Use the API from https://github.com/NicolaFerracin/michelin-stars-restaurants-api
(https://api.nicolaferracin.com/michelin/restaurants) or write another scraper.

- Use pydantic for typing, validation, data model, etc. and filter to only restaurants in London (could create another layer with all restaurants).

- Coerce data into a Google Maps-importable format. Information on importing files to a Google Maps layer (can use only up to 2000 rows per csv file):
https://support.google.com/mymaps/answer/3024836?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cstep-prepare-your-info%2Cstep-import-info-into-the-map

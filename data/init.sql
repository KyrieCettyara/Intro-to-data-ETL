CREATE TABLE IF NOT EXISTS sales(
    id SERIAL PRIMARY KEY,
    name TEXT  ,
    main_category TEXT,
    sub_category TEXT,
    image TEXT,
    link TEXT,
    ratings FLOAT,
    no_of_ratings FLOAT,
    discount_price FLOAT,
    actual_price FLOAT,
    currency TEXT,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product(
    id TEXT PRIMARY KEY,
    prices_amountMax FLOAT,
    prices_amountMin REAL,
    prices_availability TEXT,
    prices_condition TEXT,
    prices_currency TEXT,
    prices_dateSeen TEXT,
    prices_isSale BOOLEAN,
    prices_merchant TEXT,
    prices_shipping TEXT,
    prices_sourceURLs TEXT,
    asins TEXT,
    brand TEXT,
    categories TEXT,
    dateAdded TIMESTAMP,
    dateUpdated TIMESTAMP,
    imageURLs TEXT,
    keys TEXT,
    manufacturerNumber TEXT,
    name TEXT,
    primaryCategories TEXT,
    sourceURLs TEXT,
    upc TEXT,
    weight TEXT,
    weight_unit TEXT,
    created_at TIMESTAMP 
);


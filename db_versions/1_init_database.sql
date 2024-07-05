

CREATE TABLE account (
    id SERIAL PRIMARY KEY,
    user_id INT,
    balance INT
);


CREATE TABLE wallet (
    id SERIAL PRIMARY KEY,
    user_id INT,
    crypto VARCHAR(255),
    balance INT
);


CREATE TYPE invoice_status AS ENUM ('Unknown', 'Pending', 'Success', 'Failed', 'Settling', 'Settled');
CREATE TABLE invoice (
    id SERIAL PRIMARY KEY,
    fk_account INT,
    fk_wallet INT,
    buy BOOLEAN,
    amount INT,
    status invoice_status,
    CONSTRAINT fk_account FOREIGN KEY(fk_account) REFERENCES account(id),
    CONSTRAINT fk_wallet FOREIGN KEY(fk_wallet) REFERENCES wallet(id)
);

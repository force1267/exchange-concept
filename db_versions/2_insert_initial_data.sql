


INSERT INTO account (user_id, balance) VALUES (1, 1425);
INSERT INTO account (user_id, balance) VALUES (2, 11);

INSERT INTO wallet (user_id, crypto, balance) VALUES (1, 'ABAN', 12);
INSERT INTO wallet (user_id, crypto, balance) VALUES (1, 'BTC', 9);
INSERT INTO wallet (user_id, crypto, balance) VALUES (2, 'ABAN', 4);

INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (1, 1, true, 400, 'Pending');
INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (1, 2, true, 500, 'Success');
INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (1, 2, true, 600, 'Unknown');
INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (2, 3, false, 700, 'Failed');
INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (2, 3, true, 1000, 'Success');
INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (2, 3, true, 400, 'Failed');

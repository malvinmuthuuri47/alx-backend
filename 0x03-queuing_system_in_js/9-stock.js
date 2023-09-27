const express = require('express');
const app = express();
const port = 1245;
const redis = require('redis');
const client = redis.createClient();

const listProducts = [
	{ itemid: 1, itemname: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
	{ itemid: 2, itemname: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
	{ itemid: 3, itemname: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
	{ itemid: 4, itemname: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

function getItemById(id) {
	return listProducts.find((product) => product.itemid === id) || null;
}

app.listen(port, () => {
	console.log(`Server is listening on port ${port}`);
});

app.get('/list_products', (req, res) => {
	res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId);

	if (isNaN(itemId)) {
		return res.status(400).json({ error: 'Invalid itemId' });
	}

	const product = getItemById(itemId);

	console.log(product);

	if (!product) {
		return res.status(404).json({ status: 'Product not found' });
	}

	const reservedStock = await getCurrentReservedStockById(itemId);

	const result = {
		itemId: product.itemid,
		itemName: product.itemname,
		price: product.price,
		initialAvailableQuantity: product.initialAvailableQuantity,
		currentQuantity: reservedStock,
	};
	res.json(result);
});

app.get('/reserve_product/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId);

	if (isNaN(itemId)) {
		return res.status(400).json({ error: 'Invalid itemId' });
	}

	const product = getItemById(itemId);

	if (!product) {
		return res.status(404).json({ status: 'Product not found' });
	}

	const availableStock = product.initialAvailableQuantity;
	const reservedStock = await getCurrentReservedStockById(itemId);

	if (availableStock - reservedStock <= 0) {
		return res.status(400).json({ status: 'Not enough stock available', itemId: itemId });
	}

	await reserveStockById(itemId, reservedStock + 1);

	return res.json({ status: 'Reservation confirmed', itemId: itemId });
});

function reserveStockById(itemId, stock) {
	client.set(`item:${itemId}`, stock, (error, reply) => {
		if (error) {
			console.error('Error reserving stock:', error);
		} else {
			console.log(`Reserved ${stock} stock for item ${itemId}`);
		}
	});
}

async function getCurrentReservedStockById(itemId) {
	return new Promise((resolve, reject) => {
		client.get(`itemid:${itemId}`, (error, reply) => {
			if (error) {
				reject(error);
			} else {
				const reservedStock = parseInt(reply) || 0;
				resolve(reservedStock);
			}
		});
	});
}

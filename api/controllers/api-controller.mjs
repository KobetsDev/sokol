import { Product } from '../models/index.js'
import axios from 'axios'

class ApiController {
    // http://localhost:8000/api/get_products
    async get_products(req, res, next) {
        try {
            const all_products = await Product.find()
            return res.json(all_products)
        } catch (e) {
            next(e)
        }
    }
    // http://localhost:8000/api/create_link
    async create_link(req, res, next) {
        // то что приходит
        let zap = {
            "order_data":
                [{
                    "id": 123,
                    "count": 3
                }, {
                    "id": 124,
                    "count": 2
                }],
            "comment": "тут типо пожелания при заказе",
            "user_id": 569452912,
            "user_hash": null
        }
        let prices = []
        for (var key in zap.order_data) {
            console.log(zap.order_data[key].id)
            //тут поиск по id в бд
            const product = await Product.findOne({ _id: zap.order_data[key].id })
            console.log(product)
            prices.push({ 'label': product.title, 'amount': product.price })
        }
        const link = `https://api.telegram.org/bot${process.env.BOT_TOKEN}/createInvoiceLink`
        console.log(link)
        const cart = {
            'title': 'Ваш заказ',
            'description': 'За заказом подходите к баристе',
            'provider_token': process.env.PAYMENTS_PROVIDER_TOKEN,
            'currency': process.env.CURRENCY,
            'photo_url': 'https://i.ibb.co/9TDfj1G/image.png',
            'photo_height': 512,
            'photo_width': 512,
            'photo_size': 512,
            'is_flexible': false,
            'prices': JSON.stringify(prices),
            'max_tip_amount': 30_00,
            'suggested_tip_amounts': [10_00, 20_00, 30_00],
            'start_parameter': 'time-machine-example',
            'payload': 'HAPPY FRIDAYS COUPON'
        }
        // res.json('qwe')
        await axios.post(link, cart)
            .then((data) => {
                return res.json({ status: 'ok', url: data.data.result })
            }).catch((err) => {
                console.log(err)
                return res.json({ status: 'bad' })
            });
    }
}
export default new ApiController()
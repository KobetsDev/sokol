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
        let zap = req.body
        // let zap = '"[{\\"id\\":123,\\"count\\":1},{\\"id\\":124,\\"count\\":1}]"'
        console.log('zap', zap)
        // то что приходит '"[{\\"id\\":123,\\"count\\":1},{\\"id\\":124,\\"count\\":1}]"'
        // api_1     | {
        //     api_1     |   order_data: '[{"id":123,"count":1},{"id":124,"count":1}]',
        //     api_1     |   invoice: '1',
        //     api_1     |   _auth: 'query_id=AAGUNhIZAAAAAJQ2EhkRj8Ci&user=%7B%22id%22%3A420624020%2C%22first_name%22%3A%22%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22Ya_Kobets%22%2C%22language_code%22%3A%22ru%22%7D&auth_date=1659255245&hash=9cefcdee15fca7f4a517c302e06a7e40eebb7243267ae99778c335087832a9de',
        //     api_1     |   method: 'makeOrder'
        //     api_1     | }
        // let zap = {
        //     "order_data":
        //         [{
        //             "id": 123,
        //             "count": 3
        //         }, {
        //             "id": 124,
        //             "count": 2
        //         }],
        //     "comment": "тут типо пожелания при заказе",
        //     "user_id": 569452912,
        //     "user_hash": null
        // }
        let prices = []
        // console.log(zap.order_data.toString())
        zap.order_data = JSON.parse(zap.order_data.toString())
        console.log(zap.order_data)
        for (var key in zap.order_data) {
            console.log(zap.order_data[key].id)
            //тут поиск по id в бд
            const product = await Product.findOne({ _id: zap.order_data[key].id })
            console.log(product)
            prices.push({ 'label': product.title, 'amount': product.price })
        }
        const link = `https://api.telegram.org/bot${process.env.BOT_TOKEN}/createInvoiceLink`
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
            'prices': (prices),
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
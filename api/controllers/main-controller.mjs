import { Product } from '../models/index.js'

class MainController {
    // http://localhost:8000/api/get_products
    async main(req, res, next) {
        const products = await Product.find()
        for (var key in products) {
            let price = products[key].price
            if (price.toString().length >= 3) {
                products[key].price = (price / 100).toString().split('.')[0] + '.' + price.toString().slice(-2)
            } else {
                products[key].price = `0.${price}`
            }
        }
        // console.log(products)
        return res.render('index', { 'products': products })
    }

}
export default new MainController()
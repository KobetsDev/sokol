
import { Router } from 'express'
import ApiController from '../controllers/api-controller.mjs'
import MainController from '../controllers/main-controller.mjs'

const router = Router()

router.post('/api/get_products', ApiController.get_products)
router.post('/api/create_link', ApiController.create_link)
router.get('/', MainController.main)

export default router
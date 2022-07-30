import mongoose from "mongoose";

const schemaProduct = new mongoose.Schema({
    _id: {
        type: Number,
        required: true,
        unique: true,
    },
    title: {
        type: String,
        required: true,
        unique: true,
        minlength: 1
    },
    description: {
        type: String,
    },
    image_url: {
        type: String
    },
    price: {
        type: Number,
        required: true,
    }
})

export const Product = mongoose.model('Product', schemaProduct)

const schemaCart = new mongoose.Schema({
    user_id: {
        type: String,
        required: true,
        unique: true,
    },
    products: [{
        product_id: {
            type: String,
            required: true,
            unique: true
        },
        product_count: {
            type: Number,
            required: true
        }
    }],
    date_order: {
        type: Number,
        default: Date.now
    }
})

export const Cart = mongoose.model('Cart', schemaCart)


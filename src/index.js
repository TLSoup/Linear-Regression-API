import React, { useState } from 'react'
import ReactDOM from 'react-dom'
import FormRow from './FormRow'
import { Form, Button, Card, Col } from 'react-bootstrap'

const App = () => {
    return <MyForm />
}

const MyForm = () => {
    const [listingOne, setListingOne] = useState({})
    const [listingTwo, setListingTwo] = useState({})
    const [listingThree, setListingThree] = useState({})
    const [listingFour, setListingFour] = useState({})

    const updateListing = (event, row, property) => {
        switch(row) {
            case 1:
                updatePropertyForRow(listingOne, setListingOne, property, event.target.value);
                console.log(listingOne)
                break;
            case 2:
                updatePropertyForRow(listingTwo, setListingTwo, property, event.target.value);
                break;
            case 3:
                updatePropertyForRow(listingThree, setListingTwo, property, event.target.value);
                break;
            case 2:
                updatePropertyForRow(listingFour, setListingTwo, property, event.target.value);
                break;
            default:
                break;
        }
    }

    const updatePropertyForRow = (listing, setFunc, property, value) => {
        setFunc({...listing, [property]: value});
    }

    const restListings = () => {
        setListingOne({})
        setListingTwo({})
        setListingThree({})
        setListingFour({})
    }

    /**
     * MAYBE TODO: add more robust validation
     */
    const validateListing = (listing) => {
        return listing.hasOwnProperty('cost') &&
            listing.hasOwnProperty('sqft') &&
            listing.hasOwnProperty('bdrms') &&
            listing.hasOwnProperty('pool')
    }

    const validateForm = () => {
        return validateListing(listingOne) &&
            validateListing(listingTwo) &&
            validateListing(listingThree) &&
            validateListing(listingFour)
    }

    const onSubmit = () => {
        //EARLY OUT: validate form
        if (!validateForm()) {
            window.alert('Please fill out all fields')
            return;
        }

        fetch('http://localhost:5000/listings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([listingOne, listingTwo, listingThree, listingFour]),
        })
            .then((response) => {
                //successful response call setRegressionData(data) here
                console.log(JSON.stringify(response))
            })
            .catch((error) => {
                console.error(JSON.stringify(error));
            })

        console.log(listingOne)
        resetListings();
    };
    /**
     * TODO: use FormRow Component
     */
    return (
        <Card
            style={{
                maxWidth: '900px',
                marginTop: '30px',
                marginLeft: 'auto',
                marginRight: 'auto'
            }}>
            <Card.Body style={{marginRight: 'auto', marginLeft: 'auto'}}>
                <Form>
                    <Form.Row>
                        <h6>Listing #1</h6>
                    </Form.Row>
                    <FormRow row={1} handleChange={updateListing} />
                    <Form.Row>
                        <h6 style={{ marginTop: '10px' }}>Listing #2</h6>
                    </Form.Row>
                    <Form.Row>
                        <h6 style={{ marginTop: '10px' }}>Listing #3</h6>
                    </Form.Row>
                    <Form.Row>
                        <h6 style={{ marginTop: '10px' }}>Listing #4</h6>
                    </Form.Row>
                    <Form.Row style={{ float: 'right', marginTop: '20px', marginRight: '5px' }}>
                        <Button
                            variant="primary"
                            onClick={onSubmit}>
                            Submit
                        </Button>
                    </Form.Row>
                </Form>
            </Card.Body>
        </Card>
    )
}

const app = document.getElementById('app')
ReactDOM.render(<App></App>, app)
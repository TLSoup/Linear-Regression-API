import React, { useState } from 'react'
import ReactDOM from 'react-dom'
import { Form, Button, Card, Col } from 'react-bootstrap'

const App = () => {
    return (
        form()
    )
}

const form = () => {
    const [listing, setListings] = useState({
        "cost": "",
        "sqft": "",
        "bdrms": "",
        "pool": ""
    })

    const onSubmit = () => {
        fetch('http://localhost:5000/listings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(listing),
        })
            .then((response) => {
                console.log(JSON.stringify(response))
            })
            .catch((error) => {
                console.error(JSON.stringify(error));
            })

        console.log(listing)
        setListings({
            "cost": "",
            "sqft": "",
            "bdrms": "",
            "pool": ""
        })
    };

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
                    <Form.Row>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Cost</Form.Label>
                            <Form.Control placeholder="$" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Square Footage</Form.Label>
                            <Form.Control placeholder="sqft" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Bedrooms</Form.Label>
                            <Form.Control placeholder="3" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Pools (if none enter 0)</Form.Label>
                            <Form.Control placeholder="1" />
                        </Col>
                    </Form.Row>
                    <Form.Row>
                        <h6 style={{ marginTop: '10px' }}>Listing #2</h6>
                    </Form.Row>
                    <Form.Row>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Cost</Form.Label>
                            <Form.Control placeholder="$" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Square Footage</Form.Label>
                            <Form.Control placeholder="sqft" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Bedrooms</Form.Label>
                            <Form.Control placeholder="3" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Pools (if none enter 0)</Form.Label>
                            <Form.Control placeholder="1" />
                        </Col>
                    </Form.Row>
                    <Form.Row>
                        <h6 style={{ marginTop: '10px' }}>Listing #3</h6>
                    </Form.Row>
                    <Form.Row>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Cost</Form.Label>
                            <Form.Control placeholder="$" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Square Footage</Form.Label>
                            <Form.Control placeholder="sqft" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Bedrooms</Form.Label>
                            <Form.Control placeholder="3" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Pools (if none enter 0)</Form.Label>
                            <Form.Control placeholder="1" />
                        </Col>
                    </Form.Row>
                    <Form.Row>
                        <h6 style={{ marginTop: '10px' }}>Listing #4</h6>
                    </Form.Row>
                    <Form.Row>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Cost</Form.Label>
                            <Form.Control placeholder="$" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Square Footage</Form.Label>
                            <Form.Control placeholder="sqft" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Bedrooms</Form.Label>
                            <Form.Control placeholder="3" />
                        </Col>
                        <Col md="auto">
                            <Form.Label style={{ fontSize: 'small', color: 'slategray', marginBottom: 0 }}>Number of Pools (if none enter 0)</Form.Label>
                            <Form.Control placeholder="1" />
                        </Col>
                    </Form.Row>
                    <Form.Row style={{ float: 'right', marginTop: '20px', marginRight: '5px' }}>
                        <Button
                            variant="primary"
                            onClick={() => onSubmit}>
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
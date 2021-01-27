import React, { useState } from 'react'
import { Form, Button, FormLabel } from 'react-bootstrap'


const App = (() => {
  let app = {}
  app.init = () => {
    console.log('Hello World'),
      form()
  }
  const form = () => {
    const [listing, setListing] = useState({
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
      setListing({
        "cost": "",
        "sqft": "",
        "bdrms": "",
        "pool": ""
      })
    };

    return (
      <Form>
        <Form.Row>
          <Col>
            <Form.Label>Cost</Form.Label>
            <Form.Control placeholder="$" />
          </Col>
          <Col>
            <Form.Label>Square Footage</Form.Label>
            <Form.Control placeholder="sqft" />
          </Col>
        </Form.Row>
        <Form.Row>
          <Col>
            <Form.Label>Number of Bedrooms</Form.Label>
            <Form.Control placeholder="3" />
          </Col>
          <Col>
            <Form.Label>Number of Pools (if none enter 0)</Form.Label>
            <Form.Control placeholder="1" />
          </Col>
        </Form.Row>
        <Button
          variant="primary"
          onClick={() => onSubmit}>
          Submit
        </Button>
      </Form>
    )
  }

  return app
})()
document.addEventListener('DOMContentLoaded', () => {
  App.init()
})
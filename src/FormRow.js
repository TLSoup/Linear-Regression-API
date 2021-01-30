import React from 'react'
import { Form, Col } from 'react-bootstrap'

const FormRow = ({row, handleChange}) => {
    const formLabelStyle = { fontSize: 'small', color: 'slategray', marginBottom: 0 }
    const test = (e, row, property) => {
        handleChange(e, row, property)
    }
    return (
        <Form.Row>
            <Col md="auto">
                <Form.Label style={formLabelStyle}>Cost</Form.Label>
                <Form.Control placeholder="$" onChange={(e) => handleChange(e, row, 'cost')} required/>
            </Col>
            <Col md="auto">
                <Form.Label style={formLabelStyle}>Square Footage</Form.Label>
                <Form.Control placeholder="sqft" onChange={(e) => handleChange(e, row, 'sqft')} required/>
            </Col>
            <Col md="auto">
                <Form.Label style={formLabelStyle}>Number of Bedrooms</Form.Label>
                <Form.Control type="number" placeholder="3" min="0" onChange={(e) => handleChange(e, row, 'bdrms')} required/>
            </Col>
            <Col md="auto">
                <Form.Label style={formLabelStyle}>Number of Pools (if none enter 0)</Form.Label>
                <Form.Control type="number" placeholder="1" min="0" onChange={(e) => handleChange(e, row, 'pool')} required/>
            </Col>
        </Form.Row>
    )
}

export default FormRow
# Note that in the Markdown preprocessor registry, the highest
# numeric value is considered the highest priority, so the dict
# below is ordered from highest-to-lowest priority.
PREPROCESSOR_PRIORITES = {
    "generate_parameter_description": 535,
    "generate_response_description": 531,
    "generate_api_title": 531,
    "generate_api_description": 530,
    "generate_code_example": 525,
    "help_relative_links": 520,
    "setting": 515,
    "generate_return_values": 510,
    "generate_api_arguments": 505,
    "include": 500,
    "fenced_code_block": 25,
    "tabbed_sections": -500,
    "nested_code_blocks": -500,
    "emoticon_translations": -505,
}
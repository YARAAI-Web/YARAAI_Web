rule auto_rule_20250726133048_5916 {
  strings:
    $o0 = "CreateEditableStream" wide ascii nocase
  condition:
    all of them
}
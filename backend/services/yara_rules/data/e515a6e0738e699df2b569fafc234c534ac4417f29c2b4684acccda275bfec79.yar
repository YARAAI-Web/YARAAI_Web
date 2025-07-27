rule auto_rule_20250726123219_0844 {
  strings:
    $o0 = "deviceprotocol" wide ascii nocase
  condition:
    all of them
}
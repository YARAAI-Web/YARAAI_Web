rule auto_rule_20250726175013_1639 {
  strings:
    $o0 = "HexCharToByte" wide ascii nocase
  condition:
    all of them
}
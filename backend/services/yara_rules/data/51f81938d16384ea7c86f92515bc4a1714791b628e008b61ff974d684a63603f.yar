rule auto_rule_20250726115616_6244 {
  strings:
    $o0 = "xABCC77118461CEFDuLL" wide ascii nocase
  condition:
    all of them
}
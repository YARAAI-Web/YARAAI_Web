rule auto_rule_20250726200214_8883 {
  strings:
    $o0 = "dword_464108" wide ascii nocase
    $o1 = "dword_463B08" wide ascii nocase
  condition:
    all of them
}
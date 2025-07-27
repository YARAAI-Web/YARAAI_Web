rule auto_rule_20250726092859_6505 {
  strings:
    $o0 = "dword_4D3130" wide ascii nocase
    $o1 = "aIopixklzawercd" wide ascii nocase
  condition:
    all of them
}
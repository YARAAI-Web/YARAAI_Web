rule auto_rule_20250726073438_9926 {
  strings:
    $o0 = "paccel" wide ascii nocase
    $o1 = "x21A70032729DLL" wide ascii nocase
  condition:
    all of them
}
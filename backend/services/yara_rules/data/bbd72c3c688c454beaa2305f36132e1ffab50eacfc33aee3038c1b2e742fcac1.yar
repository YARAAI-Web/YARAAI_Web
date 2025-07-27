rule auto_rule_20250726165052_9294 {
  strings:
    $o0 = "dword_43EEB0" wide ascii nocase
    $o1 = "byte_433683" wide ascii nocase
  condition:
    all of them
}
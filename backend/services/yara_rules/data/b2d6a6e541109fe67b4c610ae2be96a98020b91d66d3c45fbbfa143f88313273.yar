rule auto_rule_20250726111512_9557 {
  strings:
    $o0 = "flAllocationType" wide ascii nocase
    $o1 = "dword_42796C" wide ascii nocase
  condition:
    all of them
}
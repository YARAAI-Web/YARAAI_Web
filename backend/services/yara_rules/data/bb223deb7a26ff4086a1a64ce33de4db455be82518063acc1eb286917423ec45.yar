rule auto_rule_20250727041319_1342 {
  strings:
    $o0 = "dword_441C8C" wide ascii nocase
    $o1 = "PyMem_RawFree" wide ascii nocase
  condition:
    all of them
}
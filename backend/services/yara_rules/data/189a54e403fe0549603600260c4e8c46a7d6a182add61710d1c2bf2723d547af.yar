rule auto_rule_20250726200649_1111 {
  strings:
    $o0 = "dword_46419C" wide ascii nocase
    $o1 = "nFile" wide ascii nocase
  condition:
    all of them
}
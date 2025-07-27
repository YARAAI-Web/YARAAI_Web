rule auto_rule_20250726064952_4905 {
  strings:
    $o0 = "dword_477318" wide ascii nocase
    $o1 = "dword_4772F0" wide ascii nocase
    $o2 = "x412B45" wide ascii nocase
  condition:
    3 of ($o*)
}
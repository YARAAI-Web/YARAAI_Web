rule auto_rule_20250726181616_9266 {
  strings:
    $o0 = "dword_464BD4" wide ascii nocase
    $o1 = "pHead" wide ascii nocase
    $o2 = "byte_465D61" wide ascii nocase
  condition:
    3 of ($o*)
}
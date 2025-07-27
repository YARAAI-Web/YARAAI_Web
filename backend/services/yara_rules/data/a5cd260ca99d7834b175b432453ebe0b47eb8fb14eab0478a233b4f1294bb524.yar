rule auto_rule_20250727021303_9867 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "_pLastBlock" wide ascii nocase
    $o2 = "dword_467CC0" wide ascii nocase
    $o3 = "memcpy_0" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726181811_9196 {
  strings:
    $o0 = "_read" wide ascii nocase
    $o1 = "dword_4626D0" wide ascii nocase
    $o2 = "x140u" wide ascii nocase
    $o3 = "dword_4616B8" wide ascii nocase
  condition:
    4 of ($o*)
}
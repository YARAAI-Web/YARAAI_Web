rule auto_rule_20250727035131_0662 {
  strings:
    $o0 = "dword_477234" wide ascii nocase
    $o1 = "tionAndSpinCount" wide ascii nocase
    $o2 = "byte_476F54" wide ascii nocase
  condition:
    3 of ($o*)
}
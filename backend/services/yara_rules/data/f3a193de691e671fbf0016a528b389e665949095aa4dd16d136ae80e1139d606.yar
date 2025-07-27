rule auto_rule_20250726143754_4668 {
  strings:
    $o0 = "GetStockObject" wide ascii nocase
    $o1 = "x8A8D" wide ascii nocase
    $o2 = "dword_42C00C" wide ascii nocase
    $o3 = "dword_42B01C" wide ascii nocase
    $o4 = "dword_429014" wide ascii nocase
  condition:
    4 of ($o*)
}
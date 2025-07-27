rule auto_rule_20250726092116_7030 {
  strings:
    $o0 = "x7657564u" wide ascii nocase
    $o1 = "dword_41001B" wide ascii nocase
    $o2 = "xFFFFF9A4" wide ascii nocase
    $o3 = "dword_40A650" wide ascii nocase
    $o4 = "dword_40A5B4" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726092119_9190 {
  strings:
    $o0 = "x79B1" wide ascii nocase
    $o1 = "dword_40A718" wide ascii nocase
    $o2 = "x1D12u" wide ascii nocase
    $o3 = "x4B82u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726092122_2677 {
  condition:
    auto_rule_20250726092116_7030 or auto_rule_20250726092119_9190
}
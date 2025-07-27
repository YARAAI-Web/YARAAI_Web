rule auto_rule_20250726125912_6112 {
  strings:
    $o0 = "x8FDC9A8FB91BABF2uLL" wide ascii nocase
    $o1 = "x8CCu" wide ascii nocase
    $o2 = "dword_42C701" wide ascii nocase
    $o3 = "dword_42C74D" wide ascii nocase
    $o4 = "x287Fu" wide ascii nocase
  condition:
    4 of ($o*)
}
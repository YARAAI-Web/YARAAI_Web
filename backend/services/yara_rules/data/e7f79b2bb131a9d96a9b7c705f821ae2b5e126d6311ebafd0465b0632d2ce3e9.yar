rule auto_rule_20250727021031_3781 {
  strings:
    $o0 = "byte_14001F080" wide ascii nocase
    $o1 = "x140000006LL" wide ascii nocase
    $o2 = "j_j_free" wide ascii nocase
    $o3 = "show_window_mode" wide ascii nocase
  condition:
    4 of ($o*)
}
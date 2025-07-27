rule auto_rule_20250727000359_9529 {
  strings:
    $o0 = "dword_40E000" wide ascii nocase
    $o1 = "_setenvp" wide ascii nocase
    $o2 = "finish_loop" wide ascii nocase
    $o3 = "dword_411E48" wide ascii nocase
  condition:
    4 of ($o*)
}
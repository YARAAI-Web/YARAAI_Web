rule auto_rule_20250726210024_9149 {
  strings:
    $o0 = "dword_140218468" wide ascii nocase
    $o1 = "xE91E8AF0" wide ascii nocase
    $o2 = "xC4CD90F8" wide ascii nocase
    $o3 = "xD8816263" wide ascii nocase
  condition:
    4 of ($o*)
}
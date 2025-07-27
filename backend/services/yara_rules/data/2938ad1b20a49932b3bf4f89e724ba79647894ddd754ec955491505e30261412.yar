rule auto_rule_20250727021315_6722 {
  strings:
    $o0 = "dword_7831C" wide ascii nocase
    $o1 = "dword_783F4" wide ascii nocase
    $o2 = "dword_1E6F8" wide ascii nocase
    $o3 = "x22C068" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}
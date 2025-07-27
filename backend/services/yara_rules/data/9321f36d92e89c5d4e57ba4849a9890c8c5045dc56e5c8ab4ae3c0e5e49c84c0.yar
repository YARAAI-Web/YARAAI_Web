rule auto_rule_20250727032924_5371 {
  strings:
    $o0 = "dword_427CA0" wide ascii nocase
    $o1 = "dword_427CC4" wide ascii nocase
    $o2 = "dword_427E3C" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
    $o4 = "_CopyMan" wide ascii nocase
  condition:
    4 of ($o*)
}
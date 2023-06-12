import os
import sys
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

ret = {}

with open("storage/docstore.json") as in_file:
    json_data = json.load(in_file)

for k in json_data["docstore/data"].keys():
    text = json_data["docstore/data"][k]["__data__"]["text"]

    response = openai.Completion.create(prompt="次の文章にタイトルをつけてください" + text, model="text-davinci-003")
    title = response["choices"][0]["text"].strip().strip("Title").strip("タイトル").strip(":").strip()
    ret[k] = title

    with open("storage/titles/" + k, "w") as out_file:
        out_file.write(title)
    print("finished: ", k,  " ... ", title)
sys.exit()




manual = "Previous: Builtin Features versus Extensions [Extension-Philosophy.html], Up: Advanced Features of gawk [Advanced-Features.html]  \n[Contents [index.html#SEC_Contents]][Index [Index.html]]\n\n----------------------------------------------------------------------------------------------------------------------------------\n\n\n12.9 SUMMARY\n\n * The --non-decimal-data option causes gawk to treat octal- and hexadecimal-looking input data as octal and hexadecimal. This\n   option should be used with caution or not at all; use of strtonum() is preferable. Note that this option may disappear in a\n   future version of gawk.\n * You can take over complete control of sorting in ‘for (indx in array)’ array traversal by setting PROCINFO[\"sorted_in\"] to the\n   name of a user-defined function that does the comparison of array elements based on index and value.\n * Similarly, you can supply the name of a user-defined comparison function as the third argument to either asort() or asorti() to\n   control how those functions sort arrays. Or you may provide one of the predefined control strings that work for\n   PROCINFO[\"sorted_in\"].\n * You can use the ‘|&’ operator to create a two-way pipe to a coprocess. You read from the coprocess with getline and write to it\n   with print or printf. Use close() to close off the coprocess completely, or optionally, close off one side of the two-way\n   communications.\n * By using special file names with the ‘|&’ operator, you can open a TCP/IP (or UDP/IP) connection to remote hosts on the\n   Internet. gawk supports both IPv4 and IPv6.\n * You can generate statement count profiles of your program. This can help you determine which parts of your program may be\n   taking the most time and let you tune them more easily. Sending the USR1 signal while profiling causes gawk to dump the profile\n   and keep going, including a function call stack.\n * You can also just “pretty-print” the program.\n * Persistent memory allows you to preserve the values of variables and arrays between runs of gawk. This feature is currently\n   experimental.\n * New features should be developed using the extension mechanism if possible; they should be added to the core interpreter only\n   as a last resort.\n\n----------------------------------------------------------------------------------------------------------------------------------\n\nPrevious: Builtin Features versus Extensions [Extension-Philosophy.html], Up: Advanced Features of gawk [Advanced-Features.html]  \n[Contents [index.html#SEC_Contents]][Index [Index.html]]"
manual = "Next: Probable Future Extensions [Future-Extensions.html], Previous: Downward Compatibility and Debugging\n[Compatibility-Mode.html], Up: Implementation Notes [Notes.html]   [Contents [index.html#SEC_Contents]][Index [Index.html]]\n\n----------------------------------------------------------------------------------------------------------------------------------\n\n\nC.2 MAKING ADDITIONS TO GAWK\n\nIf you find that you want to enhance gawk in a significant fashion, you are perfectly free to do so. That is the point of having\nfree software; the source code is available and you are free to change it as you want (see GNU General Public License\n[Copying.html]).\n\nThis section discusses the ways you might want to change gawk as well as any considerations you should bear in mind.\n\n * Accessing The gawk Git Repository [Accessing-The-Source.html]\n * Adding New Features [Adding-Code.html]\n * Porting gawk to a New Operating System [New-Ports.html]\n * Why Generated Files Are Kept In Git [Derived-Files.html]"
manual = "Next: The Configuration Process [Configuration-Philosophy.html], Previous: Shell Startup Files [Shell-Startup-Files.html], Up:\nCompiling and Installing gawk on Unix-Like Systems [Unix-Installation.html]   [Contents [index.html#SEC_Contents]][Index\n[Index.html]]\n\n----------------------------------------------------------------------------------------------------------------------------------\n\nB.2.3 ADDITIONAL CONFIGURATION OPTIONS\n\nThere are several additional options you may use on the configure command line when compiling gawk from scratch, including:\n\n--disable-extensions\n\nDisable the extension mechanism within gawk. With this option, it is not possible to use dynamic extensions. This also disables\nconfiguring and building the sample extensions in the extension directory.\n\nThis option may be useful for cross-compiling. The default action is to dynamically check if the extensions can be configured and\ncompiled.\n\n--disable-lint\n\nDisable all lint checking within gawk. The --lint and --lint-old options (see Command-Line Options [Options.html]) are accepted,\nbut silently do nothing. Similarly, setting the LINT variable (see Built-in Variables That Control awk [User_002dmodified.html])\nhas no effect on the running awk program.\n\nWhen used with the GNU Compiler Collection’s (GCC’s) automatic dead-code-elimination, this option cuts almost 23K bytes off the\nsize of the gawk executable on GNU/Linux x86_64 systems. Results on other systems and with other compilers are likely to vary.\nUsing this option may bring you some slight performance improvement.\n\n> CAUTION: Using this option will cause some of the tests in the test suite to fail. This option may be removed at a later date.\n\n--disable-mpfr\n\nSkip checking for the MPFR and GMP libraries. This is useful mainly for the developers, to make sure nothing breaks if MPFR\nsupport is not available.\n\n--disable-nls\n\nDisable all message-translation facilities. This is usually not desirable, but it may bring you some slight performance\nimprovement.\n\n--enable-versioned-extension-dir\n\nUse a versioned directory for extensions. The directory name will include the major and minor API versions in it. This makes it\npossible to keep extensions for different API versions on the same system without their conflicting with one another.\n\nUse the command ‘./configure --help’ to see the full list of options supplied by configure.\n\n----------------------------------------------------------------------------------------------------------------------------------\n\nNext: The Configuration Process [Configuration-Philosophy.html], Previous: Shell Startup Files [Shell-Startup-Files.html], Up:\nCompiling and Installing gawk on Unix-Like Systems [Unix-Installation.html]   [Contents [index.html#SEC_Contents]][Index\n[Index.html]]"
manual = "\"@ind_num_asc\", but the numeric indices are ordered from high to low.\n\n\"@val_type_desc\"\n\nLike \"@val_type_asc\", but the element values, based on type, are ordered from high to low. Subarrays, if present, come out first.\n\n\"@val_str_desc\"\n\nLike \"@val_str_asc\", but the element values, treated as strings, are ordered from high to low. If the string values are identical,\nthe index string values are compared instead. When comparing non-scalar values, \"@val_type_desc\" sort ordering is used, so\nsubarrays, if present, come out first.\n\n\"@val_num_desc\"\n\nLike \"@val_num_asc\", but the element values, treated as numbers, are ordered from high to low. If the numeric values are equal,\nthe string values are compared instead. If they are also identical, the index string values are compared instead. Non-scalar\nvalues are compared using \"@val_type_desc\" sort ordering, so subarrays, if present, come out first.\n\nThe array traversal order is determined before the for loop starts to run. Changing PROCINFO[\"sorted_in\"] in the loop body does\nnot affect the loop. For example:\n\n$ gawk '\n> BEGIN {\n>    a[4] = 4\n>    a[3] = 3\n>    for (i in a)\n>        print i, a[i]\n> }'\n-| 4 4\n-| 3 3\n$ gawk '\n> BEGIN {\n>    PROCINFO[\"sorted_in\"] = \"@ind_str_asc\"\n>    a[4] = 4\n>    a[3] = 3\n>    for (i in a)\n>        print i, a[i]\n> }'\n-| 3 3\n-| 4 4\n\n\nWhen sorting an array by element values, if a value happens to be a subarray then it is considered to be greater than any string\nor numeric value, regardless of what the subarray itself contains, and all subarrays are treated as being equal to each other.\nTheir order relative to each other is determined by their index strings.\n\nHere are some additional things to bear in mind about sorted array traversal:\n\n * The value of PROCINFO[\"sorted_in\"] is global. That is, it affects all array traversal for loops. If you need to change it\n   within your own code, you should see if it’s defined and save and restore the value:\n   \n   …\n   if (\"sorted_in\" in PROCINFO)\n       save_sorted = PROCINFO[\"sorted_in\"]\n   \n   PROCINFO[\"sorted_in\"] = \"@val_str_desc\" # or whatever\n   …\n   if (save_sorted)\n       PROCINFO[\"sorted_in\"] = save_sorted\n   \n\n * As already mentioned, the default array traversal order is represented by \"@unsorted\". You can also get the default behavior by\n   assigning the null string to PROCINFO[\"sorted_in\"] or by just deleting the \"sorted_in\" element from the PROCINFO array with the\n   delete statement. (The delete statement hasn’t been described yet; see The delete Statement [Delete.html].)\n\nIn addition, gawk provides built-in functions for sorting arrays; see Sorting Array Values and Indices with gawk\n[Array-Sorting-Functions.html].\n\n----------------------------------------------------------------------------------------------------------------------------------\n\nFOOTNOTES\n\n(42)\n\nWhen two elements compare as equal, the C qsort() function does not guarantee that they will maintain their original relative\norder after sorting. Using the string value to provide a unique ordering when the numeric values are equal ensures that gawk\nbehaves consistently across different environments.\n\n----------------------------------------------------------------------------------------------------------------------------------\n\nPrevious: Scanning All Elements of an Array [Scanning-an-Array.html], Up: The Basics of Arrays [Array-Basics.html]  "

prompt_prefix = "次の文章にタイトルをつけてください"
prompt_delimiter = ""


#次の文章は、gawkのマニュアルの一節です。内容を簡潔に日本語の1文で要約してください。
response = openai.Completion.create(
    prompt= prompt_prefix + prompt_delimiter + manual,
    model="text-davinci-003"
)

print(response)


#    "model": "gpt-3.5-turbo",
#    "messages": [{"role": "system", "content", ""}, {"role": "user", "content": ""}]
#  }'
